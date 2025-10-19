```json
{
  "id": "615b346df9735c07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290342,
  "host_pid": "9e6742732c60:1",
  "hash": "f4e3111de979f376e9206ba2f6f982f17dabb9e96dbd7609d613ed5886d95959",
  "cid": "QmV1f4e3111de979f376e9206ba2f6f982f17dabb9e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290342,
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
      "evaluated_at": 1760290342
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
  "sig": "dac0bf140e2682f17aeb20ed2f33cca394cb92ffd7468c87b505914e0d47bb08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035823466
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 64625680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}