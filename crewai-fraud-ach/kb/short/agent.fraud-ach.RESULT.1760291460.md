```json
{
  "id": "06341a57318b6b94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291460,
  "host_pid": "9e6742732c60:1",
  "hash": "2f48af8182fd97bc4f65005cd707d7797722de3594c3757feb2fc6321c295787",
  "cid": "QmV12f48af8182fd97bc4f65005cd707d7797722de35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291460,
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
      "evaluated_at": 1760291460
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
  "sig": "c4bc3f172a0782788f4681fffa4ef66b75ebfff789ccf9c9533708bb929b55da"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 83292475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}