```json
{
  "id": "d95b72c2dc0faf19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292741,
  "host_pid": "9e6742732c60:1",
  "hash": "2999541c5db092622de0fd35cda6f61543bbe50ab530109fca6ec56f55e869d5",
  "cid": "QmV12999541c5db092622de0fd35cda6f61543bbe50a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292741,
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
      "evaluated_at": 1760292741
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
  "sig": "86b860d93bb0500fe3f37a7c45c0512d83f5977bcc5798153e9c055a2f8a1b9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461197823
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 36800580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'c7e6425f6e43a399'}}}