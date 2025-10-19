```json
{
  "id": "d3ec4ae649a11c18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288201,
  "host_pid": "9e6742732c60:1",
  "hash": "239fc90328fcb572b19f5ed9bb0cd3291676b35fd42b79c7414d2297325b6fcb",
  "cid": "QmV1239fc90328fcb572b19f5ed9bb0cd3291676b35f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288201,
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
      "evaluated_at": 1760288201
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
  "sig": "926f81f12eaf1d9b62ae2ebb0f17ae2911007b09fd5865c0faaa8fb232dbb37e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 27412500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}