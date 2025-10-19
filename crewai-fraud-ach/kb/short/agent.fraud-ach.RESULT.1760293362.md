```json
{
  "id": "a819f4ec13a2b8b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293362,
  "host_pid": "9e6742732c60:1",
  "hash": "ec92390bc9fa10245474ccd9bc0eeacfe6265f3b2f225553ec30828ac5b719fa",
  "cid": "QmV1ec92390bc9fa10245474ccd9bc0eeacfe6265f3b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293362,
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
      "evaluated_at": 1760293362
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
  "sig": "9437c009ebcf4ef3be0770f50cf6ddabfbd1f294b133fb15c42aa5a1bd68b436"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 950960749969543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 37670115, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': 'b177ff0c3b4ad29b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '950960749', 'validation_error': 'Invalid routing number checksum'}}}