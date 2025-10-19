```json
{
  "id": "f6114ea62e457a41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288960,
  "host_pid": "9e6742732c60:1",
  "hash": "290bce91b80ba404a43594849107148d40893f001f5a5b4873e5463f4ccc9389",
  "cid": "QmV1290bce91b80ba404a43594849107148d40893f00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288960,
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
      "evaluated_at": 1760288960
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
  "sig": "e2db20aa65861e755aa07175df9c76502fcfa66c7fdc3152e5e1f185f59164c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278681806
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 51260520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '5ddc61c49d89e409'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}