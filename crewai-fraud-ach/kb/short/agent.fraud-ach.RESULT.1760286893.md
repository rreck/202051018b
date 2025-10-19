```json
{
  "id": "986b6218ba363d64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286893,
  "host_pid": "9e6742732c60:1",
  "hash": "ed31432718672af0ee3f5cefd7611738d9a318eace8172816086ddf21dd91ff8",
  "cid": "QmV1ed31432718672af0ee3f5cefd7611738d9a318ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286893,
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
      "evaluated_at": 1760286893
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
  "sig": "240eb54e9a4328adafc6b15b4c4c5b79dd10d92c410fc9de6f73a35cd72a1afe"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19910379, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}