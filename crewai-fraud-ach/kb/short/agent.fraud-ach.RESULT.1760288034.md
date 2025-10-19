```json
{
  "id": "10a07afdefa1289e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288034,
  "host_pid": "9e6742732c60:1",
  "hash": "58102a253fe8431d3aa8c49d85ab079c23d569be45339f2217bb6aec91eccdcf",
  "cid": "QmV158102a253fe8431d3aa8c49d85ab079c23d569be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288034,
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
      "evaluated_at": 1760288034
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
  "sig": "396f06bb000f1bde0ce6720efef74d9fa021022aa2333177018226977baa3374"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}