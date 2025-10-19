```json
{
  "id": "ed6c7e3a5f179987",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287901,
  "host_pid": "9e6742732c60:1",
  "hash": "1f5fc6b1413c16cccd4313f84366b993024920d9edcb3db7be9c428ddf88e59a",
  "cid": "QmV11f5fc6b1413c16cccd4313f84366b993024920d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287901,
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
      "evaluated_at": 1760287902
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
  "sig": "c3e80ed098d0579958b7d92d10f2b40955f42447900a9c2be764653cf6cf6229"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460804941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'e3b2eb0d41697d4a'}}}