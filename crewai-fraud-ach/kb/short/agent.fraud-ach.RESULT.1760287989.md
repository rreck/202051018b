```json
{
  "id": "65706d6afc61ede7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287989,
  "host_pid": "9e6742732c60:1",
  "hash": "ad7de9d1f3a49ae926fba748b8eb5ec3ffb462d3bdfd7525761d93aa9fe04df2",
  "cid": "QmV1ad7de9d1f3a49ae926fba748b8eb5ec3ffb462d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287989,
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
      "evaluated_at": 1760287989
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
  "sig": "c01b2ee7ed7b34c72ba82b4af284ca8d5626a14d172975935ecdff0c43965fa5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 27085071, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}