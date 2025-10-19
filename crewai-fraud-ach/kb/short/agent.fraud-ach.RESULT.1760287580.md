```json
{
  "id": "3a9bae0314137fc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287580,
  "host_pid": "9e6742732c60:1",
  "hash": "528eca00eb9b73a8473c934d3ee8b1f2b0e0349573dd8c82f75e4ac1f4c67d55",
  "cid": "QmV1528eca00eb9b73a8473c934d3ee8b1f2b0e03495",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287580,
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
      "evaluated_at": 1760287580
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
  "sig": "455e16b7c1d702c009368ce079ff5c9b2da566f320913bd6143069590f107443"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}