```json
{
  "id": "0062d5a61042dda8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294283,
  "host_pid": "9e6742732c60:1",
  "hash": "f0808aa974c8b5064cc97799a8530254c169b5bbe4c0821c1a29af2aa20bcf86",
  "cid": "QmV1f0808aa974c8b5064cc97799a8530254c169b5bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294283,
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
      "evaluated_at": 1760294283
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
  "sig": "632255aa310ca79d5ed9292abf139743371dbd9c9ea54ce82e3ad620b433c25a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461947560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 75962810, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': '1e39107ec95e1ca0'}}}