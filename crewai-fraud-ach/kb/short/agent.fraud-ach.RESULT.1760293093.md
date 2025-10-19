```json
{
  "id": "47b0f9b8c31bc701",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293093,
  "host_pid": "9e6742732c60:1",
  "hash": "df35b1f0761c46840e1afbda7cd84a185910ee69f97e148f5e9de5f264221f39",
  "cid": "QmV1df35b1f0761c46840e1afbda7cd84a185910ee69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293093,
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
      "evaluated_at": 1760293093
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
  "sig": "1660f9a5656f1355e09a6723e240f61e06f285fcceb10b149de966cce27ffc71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 99503169, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}