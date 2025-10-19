```json
{
  "id": "fa4a467059fc9b70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287551,
  "host_pid": "9e6742732c60:1",
  "hash": "f110db2eb03ae520a8f1e240721e707c4383cbec6c382c6935d3d269a5093318",
  "cid": "QmV1f110db2eb03ae520a8f1e240721e707c4383cbec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287551,
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
      "evaluated_at": 1760287551
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
  "sig": "e1ed8410f16157234cd125b0a7ffb51f73b872669cdf531011dbff49eb1c0a3a"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000240849779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 12361280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}