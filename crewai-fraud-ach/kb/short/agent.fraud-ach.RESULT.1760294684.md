```json
{
  "id": "fd7f5b24c0d878fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294684,
  "host_pid": "9e6742732c60:1",
  "hash": "2ab23e7aad5472e08a835fefdc3c349417126e0c93f9305f3977959d122f011f",
  "cid": "QmV12ab23e7aad5472e08a835fefdc3c349417126e0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294684,
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
      "evaluated_at": 1760294684
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
  "sig": "81576c2f5906b5784b4683d13c5d373a8bd9c6df18ad906aaf34cc8e911d094c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 77016016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}