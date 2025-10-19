```json
{
  "id": "fa74041d0a1cc6ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290657,
  "host_pid": "9e6742732c60:1",
  "hash": "948d2e0bd26964e04a6981968307f79ea37f48c2bb19776bc5286b9f2c72f456",
  "cid": "QmV1948d2e0bd26964e04a6981968307f79ea37f48c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290657,
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
      "evaluated_at": 1760290657
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
  "sig": "5ddf6fd38f73478ceb07cee025d97989ff2f790f6737fafe157884391fabb652"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662622
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 29970096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}