```json
{
  "id": "cd632631619bab31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290470,
  "host_pid": "9e6742732c60:1",
  "hash": "67e8f2bde2ace2c313dcb200ca2524727904e4125fadeb0925c14e5c435a74b9",
  "cid": "QmV167e8f2bde2ace2c313dcb200ca2524727904e412",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290470,
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
      "evaluated_at": 1760290470
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
  "sig": "301e4093fde7b0ea1226f47614274dcf7822e9337ea537d4985ad9527499630e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}een': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}