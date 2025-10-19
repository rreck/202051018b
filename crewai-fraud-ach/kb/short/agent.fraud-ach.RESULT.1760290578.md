```json
{
  "id": "c45c8b2f5d4eb674",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290578,
  "host_pid": "9e6742732c60:1",
  "hash": "ae6989b2ed22fe4012da57ede802375e0f17c927e2ba3f01412d886b25bf6d1e",
  "cid": "QmV1ae6989b2ed22fe4012da57ede802375e0f17c927",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290578,
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
      "evaluated_at": 1760290578
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
  "sig": "4f61a55a5941c0188487e119a27a3b55479143de7eae2422929642b6cc1aaefb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151540950
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 29776208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '9c022c6e80e7fcd3'}}}