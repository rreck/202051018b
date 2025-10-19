```json
{
  "id": "5b75080f27382b66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287379,
  "host_pid": "9e6742732c60:1",
  "hash": "2bd05e6aa9cd559951ab78db7fe21388a55cfd37d439118151d34809078bd6ab",
  "cid": "QmV12bd05e6aa9cd559951ab78db7fe21388a55cfd37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287379,
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
      "evaluated_at": 1760287379
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
  "sig": "154edbfede16fe6cd25a2348faf72cea4607f8db644cd975f4126e8ebe2f4f4b"
}
```

Fraud detected: duplicate_transaction (score: 75)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 66, 'details': {'transaction_count': 58, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}}een': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}