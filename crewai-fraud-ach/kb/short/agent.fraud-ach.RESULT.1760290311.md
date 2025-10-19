```json
{
  "id": "266bf828785f9142",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290311,
  "host_pid": "9e6742732c60:1",
  "hash": "7a2364c1780afb6833d2d2d46a2494619b55064ad2f20fb62d4c5b4887561fb4",
  "cid": "QmV17a2364c1780afb6833d2d2d46a2494619b55064a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290311,
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
      "evaluated_at": 1760290311
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
  "sig": "e657fc9fc097c6e7872734cbf54745706b12f330be0d363a480180499a81974a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273941483
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 46034520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '33ec4b85754ad38a'}}}