```json
{
  "id": "ef99b725713ee14d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292090,
  "host_pid": "9e6742732c60:1",
  "hash": "80f1fa63b06e6923ecb39167aad7ad5e8911d4f1cc23527ca691e7672b1456c8",
  "cid": "QmV180f1fa63b06e6923ecb39167aad7ad5e8911d4f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292090,
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
      "evaluated_at": 1760292090
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
  "sig": "117cdf7ae48d179c9139f76bd6995bef9e787c3520f72890ffca660af7dcc849"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 82509020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}