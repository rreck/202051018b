```json
{
  "id": "c7e3b9a2dbcc00c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287294,
  "host_pid": "9e6742732c60:1",
  "hash": "7e531afffe4bcb274efc09dce32bda0b448fb1592feb062b01526d03bdd13ac7",
  "cid": "QmV17e531afffe4bcb274efc09dce32bda0b448fb159",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287294,
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
      "evaluated_at": 1760287294
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "42d426c990cb16f68bec4f33fe9c214940a9ef75eccb5a6ac5371079076b9d84"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 111000023944450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': '3c29e184ba733f5e'}}}