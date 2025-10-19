```json
{
  "id": "bc1ca2a5812e04e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291351,
  "host_pid": "9e6742732c60:1",
  "hash": "613e01769cf0fee181c36a50151aa67d3ea07610929034508919ac8d5e27e809",
  "cid": "QmV1613e01769cf0fee181c36a50151aa67d3ea07610",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291351,
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
      "evaluated_at": 1760291351
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "07728d801b350cb1a146a801abaf92038821d94771b991bf228eccb9242d10b1"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 026009595171446
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 1120769082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '6f6a57bfd56698c7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6478434}}}