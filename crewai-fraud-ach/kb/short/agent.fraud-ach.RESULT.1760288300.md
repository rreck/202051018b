```json
{
  "id": "903d9c5b67d1817f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288300,
  "host_pid": "9e6742732c60:1",
  "hash": "4aae384c7e1866c4e6458288bbc5920e111424335093a94bf3ce93c49db48862",
  "cid": "QmV14aae384c7e1866c4e6458288bbc5920e11142433",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288300,
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
      "evaluated_at": 1760288300
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
  "sig": "a210a16971408aa828610205f6fe973e562d656d06cf98ca1844f123018046af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 21399516, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}