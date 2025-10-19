```json
{
  "id": "88a47d6c98a019c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292525,
  "host_pid": "9e6742732c60:1",
  "hash": "53825f09d38f4ee359af0f343079aefcfc44c544cd4cebd6d0128a791e44e552",
  "cid": "QmV153825f09d38f4ee359af0f343079aefcfc44c544",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292525,
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
      "evaluated_at": 1760292525
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
  "sig": "b45da48ebc4336be40b6269a4f87cef28917d9fba15af427df44e18fe2471770"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 91299011, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}