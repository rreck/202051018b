```json
{
  "id": "e6595e5150050bb7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289080,
  "host_pid": "9e6742732c60:1",
  "hash": "8f4a409397e0e5dc41a4888d783e7ca820896c165f8a8c75d80c199423b9ed53",
  "cid": "QmV18f4a409397e0e5dc41a4888d783e7ca820896c16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289080,
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
      "evaluated_at": 1760289080
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
  "sig": "e9975876e6c5b9757869c03a2bc971aaafb30df3b8be441e37591d0ccc0da03d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711895
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 44101188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '1e7ea83d54912238'}}}