```json
{
  "id": "0f510f193208a11c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293117,
  "host_pid": "9e6742732c60:1",
  "hash": "db40e4735231ba8c451c21e065cb3a6eafa103da76632735ff448e24943d741c",
  "cid": "QmV1db40e4735231ba8c451c21e065cb3a6eafa103da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293117,
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
      "evaluated_at": 1760293117
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
  "sig": "00d3e7fefbeb48e679065650b3d630d92204813d4c69ee72bc5fafa296ed97f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029133644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 103140968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'fa9b9676ccddb30b'}}}