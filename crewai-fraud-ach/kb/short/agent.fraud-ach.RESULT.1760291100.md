```json
{
  "id": "1282094a4535ad80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291100,
  "host_pid": "9e6742732c60:1",
  "hash": "df4d8f693380b1cbb5f39ae5700e6f61a2ba3d91d6398a2dd5cca9c6fabedca9",
  "cid": "QmV1df4d8f693380b1cbb5f39ae5700e6f61a2ba3d91",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291100,
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
      "evaluated_at": 1760291100
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
  "sig": "d4dafb55f05a239fca4d2ad1a08bb01d2865206126deb0e57e93763e08964178"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028364021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'f023f2061dd68ffa'}}}een': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}