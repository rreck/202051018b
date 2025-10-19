```json
{
  "id": "bfcdf6e657b16c4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289285,
  "host_pid": "9e6742732c60:1",
  "hash": "25515123d3b5e8006da242efc03c2de1764ab3a69a69f1b42f781657f55a5794",
  "cid": "QmV125515123d3b5e8006da242efc03c2de1764ab3a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289285,
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
      "evaluated_at": 1760289285
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
  "sig": "33eab30f0c90560b55ed61fd21808011df9df896ae6904b5973a9f700f5c0203"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158436711
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 54850075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': '839de208acaae015'}}}