```json
{
  "id": "87949a6af3629028",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289648,
  "host_pid": "9e6742732c60:1",
  "hash": "d4ba95b5b5cc5a58293233d34a2a5d25fe3f3f38046bf53a10991ae77ba40755",
  "cid": "QmV1d4ba95b5b5cc5a58293233d34a2a5d25fe3f3f38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289648,
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
      "evaluated_at": 1760289648
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
  "sig": "5241279c9eba166535baea8c76c82c905e1db6089ab3d767fbfa9b6e0146a313"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032200831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': 'cae8555d53751756'}}}een': 1760285763, 'matching_hash': '97ab95dbcdf49b98'}}}