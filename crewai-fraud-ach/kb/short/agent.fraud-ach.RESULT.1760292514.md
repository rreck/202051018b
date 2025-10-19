```json
{
  "id": "ca0a4b3a71d0803c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292514,
  "host_pid": "9e6742732c60:1",
  "hash": "26ff4401fabc5301acc994cd895724d7a205735b056d8687ee90c1307377daa9",
  "cid": "QmV126ff4401fabc5301acc994cd895724d7a205735b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292514,
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
      "evaluated_at": 1760292514
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
  "sig": "29ea96614399604b6fb6540c41be3f7d8d1248878ed06d6ad363b3eb9ad6be15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592035169
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 275, 'threshold': 50, 'total_amount': 129907525, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 274, 'first_seen': 1760284979, 'matching_hash': 'af51af40be20c608'}}}