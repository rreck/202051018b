```json
{
  "id": "aa27fcc2ace9be97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289063,
  "host_pid": "9e6742732c60:1",
  "hash": "2ff668bf0f966ba27e93833bef58d5ff6744ab34102cba738d9b06b50d81eb41",
  "cid": "QmV12ff668bf0f966ba27e93833bef58d5ff6744ab34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289063,
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
      "evaluated_at": 1760289063
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
  "sig": "fad2d7fbe9af86449d749871bce2e97641777abd78e40544337759edb94e16ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 22575952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}