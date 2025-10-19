```json
{
  "id": "5b2d0e67f7660012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292646,
  "host_pid": "9e6742732c60:1",
  "hash": "81f333063f00fb3405ad3edd7923f24499cf1413056c1c864f0dd0651985f14f",
  "cid": "QmV181f333063f00fb3405ad3edd7923f24499cf1413",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292646,
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
      "evaluated_at": 1760292646
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
  "sig": "2e9a3218e30ddd03d29cfc4989ae9cb428f38dd77df5e0c4d0ea0eeec93e5a7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245084656
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 70500424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '11924a0da29b01ce'}}}