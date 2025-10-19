```json
{
  "id": "b9f6997a6558c94d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293120,
  "host_pid": "9e6742732c60:1",
  "hash": "d95b8da8cb34a52a175454e75b9b4aa867210ef204a58e2ce5a65b306f99c1a0",
  "cid": "QmV1d95b8da8cb34a52a175454e75b9b4aa867210ef2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293120,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293121
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "91e55a3a77d218724de6b079da913b234682250dc336586e6558972ac3a6a0ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151540950
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 40990624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}