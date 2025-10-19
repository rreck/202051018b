```json
{
  "id": "2b5d60aad350752b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290869,
  "host_pid": "9e6742732c60:1",
  "hash": "bf024ea0666973d8dcf1be1b76bf18bfaa7cfcd30557232c1eba14427683cb90",
  "cid": "QmV1bf024ea0666973d8dcf1be1b76bf18bfaa7cfcd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290869,
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
      "evaluated_at": 1760290869
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
  "sig": "e69a8044c37f4da0237d9e6d617ee2cf70132bef0dadd3ad98d6a6dafd5df7a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240849779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 31096345, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}