```json
{
  "id": "97e4400654cae802",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293817,
  "host_pid": "9e6742732c60:1",
  "hash": "5a8ac4a470d1a3a165a344f1193567391106a33e7e7a041663e12243df55e4d8",
  "cid": "QmV15a8ac4a470d1a3a165a344f1193567391106a33e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293817,
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
      "evaluated_at": 1760293817
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
  "sig": "91cfab96eba9ae4ceff0a5be123faaa9fe0e91a2e00afa50cf6ee49403347257"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020823686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 14055844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '810bf9913cbceac2'}}}