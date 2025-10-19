```json
{
  "id": "d11e872f1a51ce45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287391,
  "host_pid": "9e6742732c60:1",
  "hash": "0111eab1502b301dcae965ae4dded0153c842e1feaf150c0516d38055542d393",
  "cid": "QmV10111eab1502b301dcae965ae4dded0153c842e1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287391,
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
      "evaluated_at": 1760287391
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "e8587045b220a1b9104e3e878ac1fb84a0ddb47e6d5c89ddfa67f82a454c342a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 25138302, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}