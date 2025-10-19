```json
{
  "id": "0860b789830bf4a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293210,
  "host_pid": "9e6742732c60:1",
  "hash": "b3cd773e323cb61ff29b6de8be0a3b715582200e441d4fa8b6b392b80b156de5",
  "cid": "QmV1b3cd773e323cb61ff29b6de8be0a3b715582200e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293210,
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
      "evaluated_at": 1760293210
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
  "sig": "3be2d312b2c5c69c7b5855f12768c3fa3002ae3fb6175e950bafda7afa3c2739"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 90946790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}