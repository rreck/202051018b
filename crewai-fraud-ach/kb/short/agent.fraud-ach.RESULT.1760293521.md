```json
{
  "id": "f9ad5c51b39c6591",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293521,
  "host_pid": "9e6742732c60:1",
  "hash": "28212674fb6008d3aed9905a463f513f5b6336c206d6f736503b92af536fb2bb",
  "cid": "QmV128212674fb6008d3aed9905a463f513f5b6336c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293521,
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
      "evaluated_at": 1760293521
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "5439d3162a568c8752841b32626f05e7f796d996646776e74484f56cb010d183"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105159813222
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 110000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285764, 'matching_hash': 'b185e366ced12ee8'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}