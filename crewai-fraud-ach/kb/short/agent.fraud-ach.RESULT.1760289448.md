```json
{
  "id": "45d9c285e8bfc835",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289448,
  "host_pid": "9e6742732c60:1",
  "hash": "a45202208300b7c1e009e2804328c73d08f4e079de7cc262ad86b608aecf94ee",
  "cid": "QmV1a45202208300b7c1e009e2804328c73d08f4e079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289448,
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
      "evaluated_at": 1760289448
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
  "sig": "2ab4b07df37950d01314cf986d182cf40db2a95fb89f590bd8d554c039cc12b7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 649338001689495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 40953096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '47ca0a67ca137c75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}