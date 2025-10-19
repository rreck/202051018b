```json
{
  "id": "4688c32651836547",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293706,
  "host_pid": "9e6742732c60:1",
  "hash": "c776d9b3ad7bd7937100842a5def1d00e702f6edc639a47b2bb05c18599b58da",
  "cid": "QmV1c776d9b3ad7bd7937100842a5def1d00e702f6ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293706,
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
      "evaluated_at": 1760293706
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
  "sig": "9507e2a36052dd1139cd0baa33b452340955df17fe056884cdb85d787758069e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466501917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 94479392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '521eaa6e61198532'}}}maly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6161479}}}