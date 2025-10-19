```json
{
  "id": "1c0c30aaabefee94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293115,
  "host_pid": "9e6742732c60:1",
  "hash": "86e6c97759dfac800a9d1fef683d4d774fb8027e8b914535fb39f0a542a7e08e",
  "cid": "QmV186e6c97759dfac800a9d1fef683d4d774fb8027e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293115,
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
      "evaluated_at": 1760293115
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
  "sig": "459dad33c64b564b76a98e768f36246edb2783252368706bef98accf16bade76"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248569332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 31542844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}