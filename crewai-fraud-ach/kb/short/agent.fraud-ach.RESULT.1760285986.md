```json
{
  "id": "b68cdc95d816629d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285986,
  "host_pid": "9e6742732c60:1",
  "hash": "546db2e6431d5b211015cf5caeae25e9f42ea409c8cdfe68101f05d9967ea36a",
  "cid": "QmV1546db2e6431d5b211015cf5caeae25e9f42ea409",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285986,
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
      "evaluated_at": 1760285986
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
  "sig": "449a1201290b37925dfdd3c3d5cb6ac796d504d227cbfc8945735a3a482d93d4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}