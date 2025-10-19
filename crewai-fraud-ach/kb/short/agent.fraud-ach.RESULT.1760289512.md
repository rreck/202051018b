```json
{
  "id": "5bf251e35a98ca3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289512,
  "host_pid": "9e6742732c60:1",
  "hash": "53c92e70d4741590ff76a9532a96b3472ffc4c246b5e6ff01951fc084535b12b",
  "cid": "QmV153c92e70d4741590ff76a9532a96b3472ffc4c24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289512,
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
      "evaluated_at": 1760289512
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
  "sig": "d9505763bdab617ce6b8f2a0a13c313453cb5a7df5b1ffa859e8889a8eb46177"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 58090125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}