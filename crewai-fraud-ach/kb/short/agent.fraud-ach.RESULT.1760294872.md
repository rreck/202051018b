```json
{
  "id": "ffba82cd670f401b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294872,
  "host_pid": "9e6742732c60:1",
  "hash": "51286ddee91e09d44542112faa02333ed2e0d48161be47bc0cdae2e7268fb7b1",
  "cid": "QmV151286ddee91e09d44542112faa02333ed2e0d481",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294872,
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
      "evaluated_at": 1760294873
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
  "sig": "3dade936967647969a2872a308ad618ff7b42c07ca6b991c4e2687451293f88e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596363200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 93902628, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': 'b9f8fedd6c477a32'}}}