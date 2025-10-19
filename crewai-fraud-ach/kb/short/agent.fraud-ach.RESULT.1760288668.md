```json
{
  "id": "82a62b94191443af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288668,
  "host_pid": "9e6742732c60:1",
  "hash": "0f8c5adeee002b57d0427239470ecf684a8f0f595789eb6b162e2960af02cb84",
  "cid": "QmV10f8c5adeee002b57d0427239470ecf684a8f0f59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288668,
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
      "evaluated_at": 1760288668
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
  "sig": "b5d22b5af26d9c22674d62103cb5ed7e56cd759d54955782569cc12cabc401af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 39220000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}