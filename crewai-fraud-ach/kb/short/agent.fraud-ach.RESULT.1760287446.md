```json
{
  "id": "0abe05c7ef5aedb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287446,
  "host_pid": "9e6742732c60:1",
  "hash": "a7e57f90199acc7fae8ec84da53c34d45f42a78b9a8e747b9fb43cc5ba30dc20",
  "cid": "QmV1a7e57f90199acc7fae8ec84da53c34d45f42a78b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287446,
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
      "evaluated_at": 1760287446
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
  "sig": "dd8c029e2f4234a8b12545b068cf1e9f25bf0262db49787d650f8698b41ed33b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000033294426
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': '591497f4da3dc787'}}}