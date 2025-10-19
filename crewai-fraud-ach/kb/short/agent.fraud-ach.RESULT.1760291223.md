```json
{
  "id": "d38a2c914b827403",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291223,
  "host_pid": "9e6742732c60:1",
  "hash": "4d48f5a83aad07c1fd932541dcd46514dcfb09cd585223de766b6336e03b04ab",
  "cid": "QmV14d48f5a83aad07c1fd932541dcd46514dcfb09cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291223,
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
      "evaluated_at": 1760291223
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "7bd3d57f078320e72befed9a2b8ec1b76e45fbbb28332cc178f8fc44e08425e9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244096993316032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 44176880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}