```json
{
  "id": "c37f4c3b04f154b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293803,
  "host_pid": "9e6742732c60:1",
  "hash": "24154786b669c92427e60c42e6aad22086a5da1eff80b7bbe85ff3cb7533be26",
  "cid": "QmV124154786b669c92427e60c42e6aad22086a5da1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293803,
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
      "evaluated_at": 1760293803
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
  "sig": "df22ad3c624af37beaf5a969ce8b3087d8c9851acdae3efa9e184bf9675422ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243162678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 17527430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '6908b8eed250a93e'}}}