```json
{
  "id": "f4ea43762bf02f7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289585,
  "host_pid": "9e6742732c60:1",
  "hash": "cda7a1c287882d9fd724c5bd3cace44314216f287607bd3f46112588eb30cf52",
  "cid": "QmV1cda7a1c287882d9fd724c5bd3cace44314216f28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289585,
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
      "evaluated_at": 1760289585
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
  "sig": "c1651bd16b7c44820a9ecf9eb49df680bbc5a67db00e3d2acf80cb79f27dec7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037652029
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 36237418, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '6ae01c61248929d6'}}}