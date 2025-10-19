```json
{
  "id": "01c76d9a35b090be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287824,
  "host_pid": "9e6742732c60:1",
  "hash": "9f0446793aba2e88b9725d2d3258edef17e65ba482a3f7883284c9b6f2e79abc",
  "cid": "QmV19f0446793aba2e88b9725d2d3258edef17e65ba4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287824,
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
      "evaluated_at": 1760287824
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
  "sig": "c3c1eb9187710df16cc1a4911fdff39fb0bd998d50799b5a59da4752d0fda1c8"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 23232104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}