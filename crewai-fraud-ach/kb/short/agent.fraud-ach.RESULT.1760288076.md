```json
{
  "id": "8b198f0619dc729f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288076,
  "host_pid": "9e6742732c60:1",
  "hash": "a921e0ee7aec72200db56ffda2f81efef2e651e07f4888524a172a8f434f8d57",
  "cid": "QmV1a921e0ee7aec72200db56ffda2f81efef2e651e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288076,
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
      "evaluated_at": 1760288076
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
  "sig": "24e6982d215a601142f6e29e736633e6bdcad7ea452e553f7b3ab7c0e173271e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 39916452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}