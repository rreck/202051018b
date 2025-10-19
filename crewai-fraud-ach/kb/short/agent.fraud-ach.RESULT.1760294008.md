```json
{
  "id": "4082287f46346c87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294008,
  "host_pid": "9e6742732c60:1",
  "hash": "acc146d064fd2586b1b7904f318bdf22696ce24262f08e86a5fe64021b54b643",
  "cid": "QmV1acc146d064fd2586b1b7904f318bdf22696ce242",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294008,
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
      "evaluated_at": 1760294008
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
  "sig": "a5033c3c1a977e2208879b823fe42ad5c7b447cc7ac7c9538c3f6b89a8b50977"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468983209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 65650510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}maly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}