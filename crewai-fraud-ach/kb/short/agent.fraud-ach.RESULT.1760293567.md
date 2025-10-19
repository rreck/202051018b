```json
{
  "id": "f531f59ba83dfaa5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293567,
  "host_pid": "9e6742732c60:1",
  "hash": "66f5167ced650c7546af04f4c44e27ebdad90c760621d74f64235bea02d3906a",
  "cid": "QmV166f5167ced650c7546af04f4c44e27ebdad90c76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293567,
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
      "evaluated_at": 1760293567
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
  "sig": "c24dc20082fa34b7db985b91c63b7b5b69fd77e39adf0ebc475d9175ced69ee6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 42102047, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}